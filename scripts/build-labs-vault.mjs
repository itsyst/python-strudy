import { createHash, pbkdf2Sync, randomBytes, createCipheriv } from "crypto";
import { readdirSync, readFileSync, writeFileSync, statSync } from "fs";
import { join, relative } from "path";

const ROOT = new URL("..", import.meta.url).pathname;
const LABS = join(ROOT, "labs");
const OUT = join(ROOT, "assets", "labs-vault.json");
const PEPPER = "TDDE24|python-strudy|lab-gate|2026|labs-vault";
const SALT = Buffer.from("python-strudy-labs-vault-v1");
const KEY = pbkdf2Sync(PEPPER, SALT, 120000, 32, "sha256");

function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, acc);
    else if (/\.(py|txt|md)$/i.test(name)) acc.push(p);
  }
  return acc;
}

function encrypt(text) {
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", KEY, iv);
  const enc = Buffer.concat([cipher.update(text, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return {
    iv: iv.toString("base64"),
    data: Buffer.concat([enc, tag]).toString("base64"),
  };
}

const files = {};
for (const p of walk(LABS)) {
  const rel = relative(ROOT, p).replace(/\\/g, "/");
  files[rel] = encrypt(readFileSync(p, "utf8"));
}

writeFileSync(
  OUT,
  JSON.stringify({ v: 1, algo: "AES-GCM", files: files }, null, 0),
);
console.log("vault files", Object.keys(files).length, OUT);

import { createHash } from "crypto";
import { writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const pin = process.env.TEACHER_PIN || process.argv[2] || "";
if (pin.length < 12) {
  console.error("Usage: TEACHER_PIN='…' node scripts/set-teacher-pin.mjs");
  process.exit(1);
}

const pepper = "TDDE24|python-strudy|lab-gate|2026";
const hash = createHash("sha256")
  .update(pepper + "|teacher-gate|" + pin, "utf8")
  .digest("hex");

const out = {
  v: 1,
  algo: "sha256-pepper",
  hash: hash,
  note: "SHA-256 of the teacher PIN. The PIN itself is not stored in this repo. Replace this file to reset.",
};

const file = join(dirname(fileURLToPath(import.meta.url)), "..", "assets", "teacher-gate.json");
writeFileSync(file, JSON.stringify(out, null, 2) + "\n");
console.log("wrote", file, "hash", hash.slice(0, 16) + "…");

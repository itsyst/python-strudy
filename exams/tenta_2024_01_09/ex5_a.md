Let me explain **why we need √n + 1** with a simple example!

## The problem: Why do we check up to √n?

Let's say we want to check if **36** is prime.

**All divisor pairs of 36:**
- 1 × 36
- 2 × 18
- 3 × 12
- 4 × 9
- **6 × 6** ← This is √36!
- 9 × 4
- 12 × 3
- 18 × 2
- 36 × 1

**Notice a pattern?** After we reach 6 (which is √36), the pairs just **repeat in reverse**!

- If we already checked 2, we don't need to check 18
- If we already checked 3, we don't need to check 12
- If we already checked 4, we don't need to check 9

**So we only need to check up to √36 = 6!**

---

## Why the "+1"?

This is just to be **extra safe** because of how computers handle decimal numbers.

**Example:** For n = 49
- √49 = 7.0 (exactly)
- `int(7.0)` = 7

But sometimes computers are weird with decimals:
- √49 might be calculated as 6.9999999
- `int(6.9999999)` = 6 ← **We missed 7!**

So we add +1 to make sure we don't miss anything:
- limit = 6 + 1 = 7 ✓

---

## Simple rule:

**"If a number has a divisor bigger than √n, it MUST also have a divisor smaller than √n"**

So we only check the smaller half! This makes the code **much faster** for big numbers.

**Without √n optimization:** Checking if 10000000019 is prime would test ~10 billion numbers 😱

**With √n optimization:** We only test ~100,000 numbers! ⚡
 
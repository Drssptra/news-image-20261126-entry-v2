// news-image-20261126 entry (Node 22, standard library only).
//
// The image is entry.png, rendered by generate_image.py (Pillow, system
// fonts — no network, no AI generation, so every word is exactly as written
// there). This program validates it and copies it byte for byte to the
// grader's output directory, so both runs write identical bytes.
//
// The image is a dark "ONE DAY ON EARTH" infographic summing up Thursday
// 26 November 2026 in seven stories: the Cairo tanker fire (31 killed),
// the first Trump–Xi–Putin summit, US tariffs on 14 partners, Gulf attacks,
// Ukraine strikes, the EU budget fight / new ECB chief, and a bottom strip
// on SpaceX, the Ibiza tanker and the Bangkok oil-facility fire.
//
// Local test:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576; // 1 MiB gate limit
const EXPECTED_WIDTH = 1024;
const EXPECTED_HEIGHT = 1024;

function resolveOutputDir(): string {
  return process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
}

function loadEntryPng(here: string): Buffer {
  return readFileSync(join(here, "entry.png"));
}

/** Validate the PNG before handing it over: magic, IHDR size, byte limit. */
function validatePng(png: Buffer): void {
  if (png.length < 33 || !png.subarray(0, 8).equals(PNG_MAGIC)) {
    throw new Error("entry.png is not a PNG file (bad magic bytes)");
  }
  if (png.toString("ascii", 12, 16) !== "IHDR") {
    throw new Error("entry.png has no IHDR chunk");
  }
  const width = png.readUInt32BE(16);
  const height = png.readUInt32BE(20);
  if (width !== EXPECTED_WIDTH || height !== EXPECTED_HEIGHT) {
    throw new Error(
      `entry.png is ${width}x${height}, expected ${EXPECTED_WIDTH}x${EXPECTED_HEIGHT}`,
    );
  }
  if (png.length > MAX_BYTES) {
    throw new Error(`entry.png is ${png.length} bytes, over the 1 MiB limit`);
  }
}

function render(outDir: string, png: Buffer): void {
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "entry.png"), png);
}

function main(): void {
  const here = dirname(fileURLToPath(import.meta.url));
  const png = loadEntryPng(here);
  validatePng(png);
  render(resolveOutputDir(), png);
}

main();

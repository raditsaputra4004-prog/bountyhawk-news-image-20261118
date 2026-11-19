// Entry program for news-image-20261118 (Node, standard library only).
// The image is already rendered and stored beside this file as entry.png,
// so the program just copies it into the grader's output directory.
// It runs with no network, and both runs write the identical bytes.
import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));

#!/usr/bin/env node
/**
 * Minimal lint script to forward calls to ESLint for .js, .ts, and .vue files, 
 * used when the build system calls `node lint` or `node ./lint` directly.
 */
const { spawn } = require('child_process');
const args = [
  '--ext', '.js,.ts,.vue',
  '--ignore-path', '.gitignore',
  '.'
];
const child = spawn('npx', ['eslint', ...args], { stdio: 'inherit' });

child.on('exit', code => process.exit(code));

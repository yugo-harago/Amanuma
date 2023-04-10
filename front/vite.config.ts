/// <reference types="vitest" />
import path from "path";
import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";

export default defineConfig({
  base: "/office/",
  server: {
    host: "0.0.0.0",
    port: "8080",
    strictPort: true,
    open: false,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  plugins: [
    vue(),
  ],
  test: {
    environment: "jsdom",
    testTimeout: 10000,
  },
});

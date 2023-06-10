import path from "path";
import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
import replace from "@rollup/plugin-replace";

export default defineConfig({
  base: "/office",
  server: {
    host: "0.0.0.0",
    port: 8120,
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
    replace({
      "process.env": JSON.stringify({}),
      "process.browser": true,
      preventAssignment: true,
    }),
  ],
  test: {
    environment: "jsdom",
    testTimeout: 10000,
  },
});

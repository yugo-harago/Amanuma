import path from "path";
import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
import replace from "@rollup/plugin-replace";
import vitePluginFaviconsInject from 'vite-plugin-favicons-inject';

export default defineConfig({
  base: "/",
  server: {
    host: "0.0.0.0",
    port: 8110,
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
    vitePluginFaviconsInject('./src/assets/img/Adventist_Symbol.svg'),
  ],
  test: {
    environment: "jsdom",
    testTimeout: 10000,
  },
});

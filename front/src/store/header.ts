import { defineStore } from 'pinia';

export const useHeaderStore = defineStore("header", {
  state: () => ({
    backgroundColor: 'black',
  }),
  actions: {
    setBackgroundColor(newColor) {
      this.backgroundColor = newColor;
    },
  },
});
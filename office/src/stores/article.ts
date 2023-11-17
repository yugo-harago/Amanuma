import axios from 'axios'
import { defineStore } from 'pinia'
import { Article } from '@/types/article'
import consts from '@/consts/consts.ts'

interface ModuleState {
  articleList: Article[]
  errors: any
}

export const useArticleStore = defineStore('article', {
  state: (): ModuleState => ({
    articleList: [],
    errors: {},
  }),
  actions: {
    fecthArticleList(length: number) {
      return axios
        .get(`${consts.BASE_URL}/article/?limit=${length ?? '10'}`)
        .then(({ data }) => {
          this.articleList = data
        })
    },
    postArticle(payload: any) {
      return axios
        .post(`${consts.BASE_URL}/article/`, payload)
        .then(({ data }) => {
          this.errors = {}
        })
        .catch((err) => {
          this.errors = err.response.data
        })
    },
    deleteArticle(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/article/${id}/`)
        .then(({ data }) => {
          this.errors = {}
        })
        .catch((err) => {
          this.errors = err.response.data
        })
    }
  },
})

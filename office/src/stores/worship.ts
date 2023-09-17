import axios from 'axios'
import { defineStore } from 'pinia'
import { WorshipInfo, WorshipInfoHistory } from '@/types/news'
import consts from '@/consts/consts.ts'

interface ModuleState {
  worshipInfo: WorshipInfo,
  worshipInfoHistory: WorshipInfoHistory,
  errors: any
}

export const useWorshipStore = defineStore('worship', {
  state: (): ModuleState => ({
    worshipInfo: {},
    worshipInfoHistory: [],
    errors: {},
  }),
  actions: {
    fecthWorshipInfo() {
      return axios
        .get(`${consts.BASE_URL}/api/worship-info/`)
        .then(({ data }) => {
          if (!data.info) {
            data = 
            {
              info:[
                {
                    id: '1',
                    weekday: 'sat',
                    name: '土曜日プログラム',
                    events: [
                        {
                            name: '安息日学校礼拝',
                            startTime: "09:00",
                            endTime: "12:00",
                            subEvents: [{
                                name: '司会',
                                responsible: '司会者さん'
                            }]
                        },
                        {
                            name: '休憩',
                            startTime: "10:40",
                            endTime: "10:50"
                        },
                        {
                            name: '教会発表',
                            startTime: "10:50",
                            endTime: "11:00"
                        },
                        {
                            name: '礼拝',
                            startTime: "09:00",
                            endTime: "12:00",
                            subEvents: [{
                                name: '安息日学校',
                                responsible: '近藤先生'
                            }]
                        }
                    ]
                }
              ]
            }
          }
          this.worshipInfo = data
          
        })
    },
    fecthWorshipInfoHistory(length: number) {
      return axios
        .get(`${consts.BASE_URL}/worship-infos/?limit=${length ?? '10'}`)
        .then(({ data }) => {
            this.worshipInfoHistory = data
        })
    },
    saveWorshipInfo(payload: any) {
      return axios
        .put(`${consts.BASE_URL}/worship-info/`, payload)
        .then(({ data }) => {
            this.worshipInfo = data
            this.errors = {}
        })
        .catch((err) => {
            this.errors = err.response.data
        })
    },
  },
})

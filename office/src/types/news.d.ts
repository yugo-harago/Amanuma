export interface Link {
  text: string
  url: string
}

export interface News {
  id: string
  date: string
  title: string
  author: string
  submitter: string
  content: string
  links: Link[]
}

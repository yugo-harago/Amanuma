
export interface WorshipSubEvent {
    eventName: string;
    responsible: string;
}

export interface WorshipMainEvent {
    startTime: string;
    endTime: string;
    subEvents?: WorshipSubEvent[];
}

export interface WorshipInfo {
    id: string
    weekday: string
    events: WorshipMainEvent[]
}
  
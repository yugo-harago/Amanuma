
export interface WorshipInfo {
    id: string
    weekday: string
    events: WorshipMainEvent[]
}

export interface WorshipMainEvent {
    startTime: string;
    endTime: string;
    subEvents?: WorshipSubEvent[];
}

export interface WorshipSubEvent {
    eventName: string;
    responsible: string;
}

export interface WorshipInfoHistory {
    id: string
    worshipInfo: WorshipInfo;
    createdDate: string;
}

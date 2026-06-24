export interface TopologyNode {
    id: string;
}

export interface TopologyLink {
    source: string;
    target: string;
}

export interface TopologyResponse {
    nodes: TopologyNode[];
    links: TopologyLink[];
}
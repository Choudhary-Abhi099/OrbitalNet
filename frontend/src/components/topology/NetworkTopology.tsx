import { useEffect, useState } from "react";

import ReactFlow, {
    Controls,
    Background
} from "reactflow";

import type {
    Node,
    Edge
} from "reactflow";

import "reactflow/dist/style.css";

import type {
    TopologyResponse
} from "../../types/topology";

export default function NetworkTopology() {

    const [nodes, setNodes] =
        useState<Node[]>([]);

    const [edges, setEdges] =
        useState<Edge[]>([]);

    useEffect(() => {

        const fetchTopology =
            async () => {

                const response =
                    await fetch(
                        "http://127.0.0.1:8000/network/topology"
                    );

                const data:
                    TopologyResponse =
                    await response.json();

                const flowNodes =
                    data.nodes.map(
                        (
                            node,
                            index
                        ) => ({
                            id: node.id,

                            data: {
                                label:
                                    node.id
                            },

                            position: {
                                x:
                                    (index % 15)
                                    * 150,

                                y:
                                    Math.floor(
                                        index / 15
                                    ) * 100
                            }
                        })
                    );

                const flowEdges =
                    data.links.map(
                        (
                            link,
                            index
                        ) => ({
                            id:
                                `e-${index}`,

                            source:
                                link.source,

                            target:
                                link.target
                        })
                    );

                setNodes(
                    flowNodes
                );

                setEdges(
                    flowEdges
                );
            };

        fetchTopology();

    }, []);

    return (

        <div
            className="
                h-200
                bg-slate-900
                rounded-xl
            "
        >

            <ReactFlow
                nodes={nodes}
                edges={edges}
                fitView
            >

                <Background />

                <Controls />

            </ReactFlow>

        </div>
    );
}
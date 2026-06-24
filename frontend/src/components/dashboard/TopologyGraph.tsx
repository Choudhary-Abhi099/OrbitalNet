import ReactFlow, {
    Background,
    Controls
} from "reactflow";

import "reactflow/dist/style.css";

import {
    useTopology
} from "../../hooks/useTopology";

export default function TopologyGraph() {

    const topology =
        useTopology();

    if (!topology) {

        return (
            <div>
                Loading...
            </div>
        );
    }

    const nodes =
        topology.nodes.map(
            (node, index) => ({

                id: node.id,

                data: {
                    label: node.id
                },

                position: {

                    x:
                        (index % 15) * 120,

                    y:
                        Math.floor(
                            index / 15
                        ) * 80
                }
            })
        );

    const edges =
        topology.links.map(
            (link, index) => ({

                id:
                    `edge-${index}`,

                source:
                    link.source,

                target:
                    link.target
            })
        );

    return (

        <div
            className="
                h-full
                w-full
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
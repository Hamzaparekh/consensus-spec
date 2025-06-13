from graphviz import Digraph

def diagram_deneb(path="deneb_benchmark"):
    dot = Digraph(comment="Ethereum Deneb Benchmark Flow", format="svg")
    dot.attr(rankdir="TB", fontsize="12", fontname="Helvetica", bgcolor="white")

    # nodes
    dot.node("A", "Start: for each payload size & iteration", shape="box")
    dot.node("B", "Generate 5 random payloads", shape="box")
    dot.node("C", "Build empty block for slot+1\nInsert dummy BLS & KZG proofs", shape="box")
    dot.node("D", "Record mem_before\nStart timer", shape="box")
    dot.node("E", "spec.process_block(state, block)", shape="box")
    dot.node("F", "Stop timer\nRecord mem_after & CPU%", shape="box")
    dot.node("G", "Compute latency & log CSV row", shape="box")
    dot.node("H", "More iterations?", shape="diamond")
    dot.node("I", "End", shape="oval")

    # edges
    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")
    dot.edge("E", "F")
    dot.edge("F", "G")
    dot.edge("G", "H")
    dot.edge("H", "A", label="yes")
    dot.edge("H", "I", label="no")

    dot.render(path, view=False)
    print(f"Deneb diagram written to {path}.svg")

def diagram_rapidchain(path="rapidchain_benchmark"):
    dot = Digraph(comment="RapidChain Benchmark Flow", format="svg")
    dot.attr(rankdir="TB", fontsize="12", fontname="Helvetica", bgcolor="white")

    dot.node("A", "Init: register & build RapidchainConsensus", shape="box")
    dot.node("B", "for each payload size & round", shape="box")
    dot.node("C", "Generate & concat 5 random chunks", shape="box")
    dot.node("D", "Build block struct\n(Round, Issuer, Payload, PrevHash)", shape="box")
    dot.node("E", "IsLeader?\n(Propose vs Decide)", shape="diamond")
    dot.node("F1", "Propose():\n– Emulate cost\n– Chunk & sign\n– PROPOSE vote", shape="box")
    dot.node("F2", "Decide():\n– Wait & participate\n– echo/accept votes", shape="box")
    dot.node("G", "Measure latency, CPU%, mem\nCompute throughput", shape="box")
    dot.node("H", "Advance prevHash & round", shape="box")
    dot.node("I", "More rounds?", shape="diamond")
    dot.node("J", "End", shape="oval")

    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")
    dot.edge("E", "F1", label="yes")
    dot.edge("E", "F2", label="no")
    dot.edge("F1", "G")
    dot.edge("F2", "G")
    dot.edge("G", "H")
    dot.edge("H", "I")
    dot.edge("I", "B", label="yes")
    dot.edge("I", "J", label="no")

    dot.render(path, view=False)
    print(f"RapidChain diagram written to {path}.svg")

def diagram_elastico(path="elastico_benchmark"):
    dot = Digraph(comment="Elastico Benchmark Flow", format="svg")
    dot.attr(rankdir="TB", fontsize="12", fontname="Helvetica", bgcolor="white")

    dot.node("A", "for each payload size & iteration", shape="box")
    dot.node("B", "Measure CPU before\nStart timer", shape="box")
    dot.node("C", "Repeat 5×:\nrunElasticoTransaction(size)", shape="box")
    dot.node("D", "runElasticoTransaction():\n– NewIDProof\n– simulateCommitteePBFT()", shape="box")
    dot.node("E", "simulateCommitteePBFT():\n3 PBFT phases\n(dummy compute + sleep 50ms)", shape="box")
    dot.node("F", "Stop timer\nMeasure CPU after & mem", shape="box")
    dot.node("G", "Compute latency & log CSV row", shape="box")
    dot.node("H", "More iterations?", shape="diamond")
    dot.node("I", "End", shape="oval")

    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")
    dot.edge("E", "C", label="next tx")
    dot.edge("C", "F", label="after 5 tx")
    dot.edge("F", "G")
    dot.edge("G", "H")
    dot.edge("H", "A", label="yes")
    dot.edge("H", "I", label="no")

    dot.render(path, view=False)
    print(f"Elastico diagram written to {path}.svg")

if __name__ == "__main__":
    diagram_deneb()
    diagram_rapidchain()
    diagram_elastico()

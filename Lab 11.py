from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    root = MindMapComposite("MindMap", "circle")

    origins = MindMapComposite("Origins", "oval")
    origins.add(MindMapLeaf("Long history", "plain"))
    origins.add(MindMapLeaf("::icon(fa fa-book)", "plain"))
    origins.add(MindMapLeaf("Popularisation", "plain"))
    root.add(origins)

    research = MindMapComposite("Research", "cloud")
    research.add(MindMapLeaf("On effectiveness and features", "plain"))
    research.add(MindMapComposite("On Automatic creation", "square"))
    root.add(research)

    tools = MindMapComposite("Tools", "bang")
    tools.add(MindMapLeaf("Pen and paper", "plain"))
    tools.add(MindMapLeaf("Mermaid", "plain"))
    root.add(tools)

    root.display()

if __name__ == "__main__":
    main()

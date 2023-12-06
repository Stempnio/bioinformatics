from Bio import Phylo

if __name__ == "__main__":
    tree = Phylo.read("tree.ph", "newick")

    terminals = tree.get_terminals()

    terminals = [x for x in terminals if x.name != 'Homo']

    for terminal in terminals:
        distance = tree.distance("Homo", terminal.name)
        print(f'Distance to {terminal.name}: {distance}')

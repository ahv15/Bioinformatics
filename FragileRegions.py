def ChromosomeToCycle(c):
    Nodes=[]
    for i in range (0,len(c)):
        j=c[i];
        if (int(j)>0):
            Nodes.append(2*int(j)-1)
            Nodes.append(2*int(j))
        else:
            Nodes.append(-2*int(j))
            Nodes.append(-2*int(j)-1)
    return Nodes

def CycleToChromosome(Nodes):
    c=[]
    for i in range(0,int(len(Nodes)/2)):
        if (Nodes[2*i]<Nodes[2*i+1]):
            c.append(int(Nodes[2*i+1]/2))
        else:
            c.append(int(-Nodes[2*i]/2))
    return c

def ColoredEdges(P):
    edges=[]
    for chromosome in P:
        Nodes=ChromosomeToCycle(chromosome)
        for j in range(0,len(chromosome)):
            pair=(Nodes[2*j+1],Nodes[(2*j+2)%len(Nodes)])
            edges.append(tuple(pair))
    return tuple(edges)

def GraphToGenome(Graph):
        genome = []
        init = Graph[0][0]
        if (init%2 == 0):
            end = init-1
        else:
            end = init+1
        p = []
        i=0
        while(True):
            if (init%2 == 0):
                p.append(int(init/2))
            else:
                p.append(int(-(init+1)/2))
            next1 = Graph[i][1]
            if (next1 == end):
                genome.append(tuple(p))
                if(i==len(Graph)):
                    break
                i=i+1
                if(i==len(Graph)):
                    break
                init=Graph[i][0]
                if (init%2 == 0):
                    end = init-1
                else:
                    end = init+1
                p=[]
                continue
            i=i+1
            init=Graph[i][0]
        return tuple(genome)


def TwoBreakGenomeGraph(genome,a,b,c,d):
    cgenome=[]
    for g in genome:
        if(g==(a,b)):
            cgenome.append((a,c))
        elif(g==(b,a)):
            cgenome.append((b,d))
        elif(g==(c,d)):
            cgenome.append((c,a))
        elif(g==(d,c)):
            cgenome.append((d,b))
        else:
            cgenome.append(g)
    return cgenome

def TwoBreakOnGenome(genome,a,b,c,d):
    g=ColoredEdges(genome)
    g=TwoBreakOnGenomeGraph(g,a,b,c,d)
    genome=GraphToGenome(g)
    return genome

                

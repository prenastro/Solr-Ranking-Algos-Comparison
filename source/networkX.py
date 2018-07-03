import networkx as nw

Graph =nw.read_edgelist('edgeList.txt')
page_rank = nw.pagerank(Graph, alpha=0.85, personalization=None, max_iter=30, tol=1e-06, nstart=None, weight='weight', dangling=None)
fp = open('external_pageRankFile.txt', 'w+')
for val in Graph:
    fp.write('/Users/prerana/Desktop/solr-7.3.0/NBC_News/'+val+'='+str(page_rank[val])+'\n')
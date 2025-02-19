from AlgorithmLibrary import *
from MLLibrary import *
import time

""" Algorithm Library Testing """
def main():

    # print(f"Testing TrieTagger...")
    # tagList = ["hello", "world", "!"]
    # tagger = TrieTagger(tagList, tokenizer=TrieTagger.WordTokenizer)
    # print(tagger.tag("TESTING: hello world !"))

    # print(f"Testing HeapCache...")
    # heap = HeapCache(reverse=False, capacity=4)
    # print(f"Empty Heap: ", heap)
    # heap.insertData("a", "a", 10)
    # heap.insertData("b", "b", 1)
    # heap.insertData("c", "c", 12)
    # heap.insertData("d", "d", 30)
    # heap.insertData("e", "e", -3)
    # print(f"Insertion + Overflow Test: ", heap)
    # heap.popData("c")
    # heap.popData("e")
    # print(f"Deletion Test: ", heap)
    # print(f"HeapSort Test: ", heap.__repr__(False))
    # testCache = [
    #     HeapCache.Data("a", "a", 10, 0),
    #     HeapCache.Data("b", "b", 1, 1),
    #     HeapCache.Data("c", "c", 12, 2),
    #     HeapCache.Data("d", "d", 30, 3),
    #     HeapCache.Data("e", "e", -3, 4)
    # ]
    # heap.heapify(cache=testCache)
    # print(f"Heapify Test: " + str([f"({x.getData()}, {x.getOrder()}, {x.getIndex()})" for x in testCache]))

    # print(f"Testing QuickSort...")
    # a = [12,1,-20,50,12,12,12,13481,3,-1324,5]
    # b = []
    # QuickSort.sort(a, reverse=True)
    # print(a)
    # QuickSort.sort(a, reverse=False)
    # print(a)
    # QuickSort.sort(b, reverse=False)
    # print(b)

    # print(f"Testing BinarySearchTree...")
    # bst = BinarySearchTree()
    # print(bst)
    # bst.insert(2)
    # bst.insert(-1)
    # bst.insert(5)
    # bst.insert(-10)
    # bst.insert(4)
    # bst.insert(0)
    # print(bst)
    # print(bst.search(4).getData())
    # print(bst.search(2000))
    # # Test isBST.
    # root = BinarySearchTree.Node(2)
    # n1 = BinarySearchTree.Node(-1)
    # n2 = BinarySearchTree.Node(5)
    # n3 = BinarySearchTree.Node(-10)
    # n4 = BinarySearchTree.Node(4)
    # n5 = BinarySearchTree.Node(0)
    # n6 = BinarySearchTree.Node(2000)
    # root.setLeft(n1)
    # root.setRight(n4)
    # n1.setLeft(n3)
    # n1.setRight(n5)
    # # n4.setLeft(n2)
    # n4.setRight(n6)
    # print(BinarySearchTree.isBST(root))

    # print(f"Testing LinkedList...")
    # ll = LinkedList()
    # ll.append(LinkedList.Node("1"))
    # ll.append(LinkedList.Node("2"))
    # ll.append(LinkedList.Node("3"))
    # ll.append(LinkedList.Node("4"))
    # ll.append(LinkedList.Node("5"))
    # print(ll)
    # ll.delete("3")
    # print(ll)
    # ll.swap("5", "2")
    # print (ll)
    # ll.reverse()
    # print(ll)
    # ll.clear()
    # print(ll)
    # ll.reverse()
    # print(ll)

    # print(f"Testing FibonacciCache...")
    # fc = FibonacciCache()
    # t1 = time.time()
    # fc.fibonacci(2500)
    # t2 = time.time()
    # print(f"{fc} | Time Spent: {t2-t1} sec")
    # t3 = time.time()
    # fc.fibonacci(5000)
    # t4 = time.time()
    # print(f"{fc} | Time Spent: {t4-t3} sec")
    # recNum = 25
    # t5 = time.time()
    # fc.fibonacci(recNum, False)
    # t6 = time.time()
    # print(f"Fibonacci Number {recNum}: {fc.fiboCache[recNum]} | Recursive Time Spent: {t6-t5} sec")

    # print(f"Testing TarjanSCC()...")
    # G = [
    #     [1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1],
    #     [0, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 0],
    #     [1, 0, 0, 1, 1],
    # ]
    # t = TarjanSCC(G)
    # scc = t.tarjan_dfs(reverse=False)
    # print(scc)
            
    # print(f"Testing DijkstraBFS()...")
    # G = [
    #     [0, 1, 0, 0, 0],
    #     [1, 0, 0, 0, 0],
    #     [0, 0, 0, 5, 0],
    #     [0, 0, 1, 0, 1],
    #     [0, 0, -2, -4, 0],
    # ]
    # d = DijkstraBFS(G, maximal=False)
    # dist, path = d.bfs()
    # print(dist)
    # print(path)

    # print(f"Testing KruskalMST()...")
    # G = [
    #     [0, 1, -1, 1, 0],
    #     [1, 0, 1, 1, 2],
    #     [4, 2, 0, 5, 0],
    #     [1, -1, 1, 0, 0],
    #     [7, 0.5, -2, -4, 0],
    # ]
    # d = KruskalMST(G, maximal=True)
    # tree, score = d.mst()
    # print(tree)
    # print(score)

    # print(f"Testing KnapSack()...")
    # VALUE = [4, 2, 1, 6, 7]
    # COST = [2, 2, 3, 4, 5]
    # ks = KnapSack(VALUE, COST, weight=8, repetition=False)
    # print(ks.compute_knapsack())

    # print(f"Testing LevenshteinDP()...")
    # ld = LevenshteinDP("hello", "brushllw")
    # print(ld.edit_distance())

    # print(f"Testing WaterCapture()...")
    # BARS = [ 4, 2, 1, 3, 0, 1 ]
    # wc = WaterCapture(BARS)
    # print(wc.water_volume())
    # print(wc.water_volume_alt())

    # print(f"Testing Numerics...")
    # nmrcs = Numerics()
    # SEED = 0
    # N = 100
    # K = 10
    # # Sample
    # print(nmrcs.randomSample(N, K, SEED))
    # # Shuffle
    # print(nmrcs.randomSample(N, N, SEED))
    # S = 100000
    # count = 0
    # for _ in range(S):
    #     x = nmrcs.randNFromRandK(n=N, k=K)
    #     if x == 0:
    #         count += 1
    # print(f"Expected Probability: {1 / N} | Experimental Ratio: {count / S}")

    # l = [1,2,3,4,5,6,7]
    # print(nmrcs.triangleAverage(l))
    # print(nmrcs.triangleVariance(l))
    # print(
    #     nmrcs.movingMedian(0),
    #     nmrcs.movingMedian(6),
    #     nmrcs.movingMedian(-10),
    #     nmrcs.movingMedian(19),
    #     nmrcs.movingMedian(4),
    #     nmrcs.movingMedian(-5),
    # )
    # print(nmrcs.maxHeap, nmrcs.minHeap)
    # nmrcs.clearMedianCache()
    # print(nmrcs.maxHeap, nmrcs.minHeap)

    # print(f"Testing CombinatorialTokenizer...")
    # tokenList = ["c", "ca", "th", "at", "he", "r", "i", "ne", "n", "e", "ly"]
    # tPart = CombinatorialTokenizer(tokenList)
    # print(tPart)
    # EX1 = "CAthErinE"
    # EX2 = "cAitlYn"
    # t1 = time.time()
    # tPart.tokenize(EX1 * 8, cache=False)
    # t2 = time.time()
    # tPart.tokenize(EX1 * 8, cache=True)
    # t3 = time.time()
    # print(tPart.tokenize(EX1))
    # print(tPart.tokenize(EX2))
    # print(f"Non-Cached Speed: {t2-t1} | Cached Speed: {t3-t2}")

    """ Machine Learning Library Testing """

    # print(f"Testing Transformer(Module)...")
    # SEED = 42
    # prompt = torch.tensor([
    #     [1,2,3,4,5],
    #     [6,7,8,9,10]
    # ])
    # response = torch.tensor([
    #     [11,12,13,14,15],
    #     [16,17,18,19,20]
    # ])
    # dual = torch.tensor([
    #     [
    #         [1,2,3,4,5],
    #         [11,12,13,14,15]
    #     ], [
    #         [6,7,8,9,10],
    #         [16,17,18,19,20]
    #     ]
    # ])
    # promptDataset, responseDataset = TokenSequence.dualTokenSequence(dual, shuffle=True, seed=SEED)
    # # for dataset in [promptDataset, responseDataset]:
    # #     print(f"{dataset.getX()}\n{dataset.getY()}\n{dataset.getMask()}\n{dataset[1]}")

    # tx: Transformer = Transformer(stack=1, seed=SEED)
    # print(tx(promptDataset.getX(), responseDataset.getX(), promptDataset.getMask(), responseDataset.getMask()))
    # tx.train(trainData=dual, evalData=dual, numEpoch=25, batchSize=16, lr=1e-2, seed=SEED)

    # # Input Q, K, and V
    # q = torch.tensor([
    #     [[1.0,2.0,3.0,4.0],
    #      [1.0,5.0,3.0,4.0],
    #      [1.0,2.0,3.0,4.0]]
    # ], requires_grad=True)
    # k = torch.tensor([
    #     [[1.0,2.0,3.0,10.0],
    #      [1.0,2.0,3.0,-1.0],
    #      [1.0,2.0,-3.0,2.5],
    #      [-5.0,2.0,-3.0,7.0]]
    # ], requires_grad=True)
    # v = torch.tensor([
    #     [[1.0,-2.0,3.0,-4.0],
    #      [1.0,2.0,9.0,-27.0],
    #      [1.0,2.0,3.0,20.0],
    #      [-1.0,15.0,3.0,-2.5]]
    # ], requires_grad=True)
    # qkMask = torch.tensor([
    #     [[1.0, 1.0, 1.0, 0.0],
    #      [1.0, 1.0, 0.0, 1.0],
    #      [1.0, 0.0, 1.0, 1.0]]
    # ])
    # gradOutput = torch.tensor([
    #     [[1.0,2.0,3.0], [1.0,2.0,3.0], [1.0,2.0,3.0]]
    # ], requires_grad=True)

    # # Test MultiHeadAttention(Module).
    # multiAtx = MultiHeadAttention(q.shape[-1], k.shape[-1], v.shape[-1], heads=2)
    # output = multiAtx(q,k,v,qkMask)
    # print(output)

    # # Compare Attention() with torch.nn.functional.scaled_dot_product_attention().
    # atx = Attention()
    # output = atx.apply(q,k,v,qkMask)
    # print(output)
    # gradTest = torch.autograd.grad(output, (q,k,v), gradOutput)
    # print(gradTest)
    # realAtx = torch.nn.functional.scaled_dot_product_attention(q, k, v, attn_mask=qkMask)
    # print(realAtx)
    # gradTest = torch.autograd.grad(realAtx, (q,k,v), gradOutput)
    # print(gradTest)

    # posEnc = PositionEncoder(3, 5)
    # print(posEnc.positionalEncoding)
    # testTensor = torch.tensor([
    #     [0.0,1.0,2.0,3.0,4.0],
    #     [0.0,1.0,2.0,3.0,4.0],
    #     [0.0,1.0,2.0,3.0,4.0],
    # ])
    # print(posEnc(testTensor))

    # print(f"Testing GaussianMixture...")
    # SEED = 4
    # SHAPE = (10, 2)
    # rng = np.random.default_rng(SEED)
    # NORM = 1
    # D = 2 * NORM * (rng.random(SHAPE) - 0.5)
    # K = 3
    # GMM = GaussianMixture(data=D, k=K, seed=SEED)
    # GMM.fit()

    # # Battle-Testing
    # sims = [0, 500]
    # count = 0
    # seedset = set()
    # SHAPE = (10, 2)
    # NORM = 1
    # K = 3
    # for seed in range(*sims):
    #     # Generate data.
    #     rng = np.random.default_rng(seed)
    #     D = 2 * NORM * (rng.random(SHAPE) - 0.5)
    #     # Fit data.
    #     GMM = GaussianMixture(data=D, k=K, seed=seed)
    #     GMM.fit()
    #     # Analyze results.
    #     if math.isnan(GMM.modelDelta):
    #         seedset.add(seed)
    #     else:
    #         count += 1
    # print(f"Numerical Convergence Ratio: {count / (sims[1] - sims[0])}")
    # print(f"Broken Seeds: {seedset}")

    # print(f"Testing MatrixFactorize...")
    # SEED = 0
    # SHAPE = (5,9)
    # rng = np.random.default_rng(SEED)
    # M = rng.integers(100, size=SHAPE)
    # Z = 3
    # m = MatrixFactorize(
    #     M,
    #     Z,
    #     mask=rng.integers(2, size=SHAPE),
    #     bias=True,
    #     seed=SEED
    # )
    # m.fit()
    # print(m)

    # print(f"Testing FactorizationMachine...")
    # SEED = 0
    # N = 1000
    # X = 10
    # T = 1
    # H = 10
    # VALUES = (-100, 100)
    # rng = np.random.default_rng(SEED)
    # INPUT = (VALUES[1] - VALUES[0]) * rng.random(size=(N,X)) + VALUES[0]
    # TARGET = rng.integers(2, size=(N,T))
    # fm = FactorizationMachine(
    #     X, H, seed=SEED
    # )
    # fm.fit(
    #     INPUT,
    #     TARGET,
    #     mask=rng.integers(2, size=(N,X)),
    #     cycles=100,
    #     lr=2e-3,
    #     batch_frac=0.01,
    #     regularize=1e-2,
    #     patience=5,
    #     verbose=True
    # )

if __name__ == "__main__":
    main()
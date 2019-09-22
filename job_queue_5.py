#Python3

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        self.resultlist = []
        self.jobtime = 0
        self.workers = []
        self.jobs = []
        self.job = 0
        self.worker = 0
    
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      return self.heapList
    
    def build_pq(self,jobs,workers):
        self.workers = list(range(workers))
        self.jobs = jobs
        while len(self.jobs) > 0:

            #process jobs from queue
            while len(self.workers) > 0 \
            and len(self.jobs) > 0:
                self.job = self.jobs.pop(0) + self.jobtime  #time job will end
                self.worker = self.workers.pop(0)           #next worker
                self.insert((self.job, self.worker, self.jobtime)) #add processed job onto heap
                self.resultlist.append((self.worker, self.jobtime)) #record worker and processing time
            self.jobtime = self.heapList[1][0] #increment the start time for next jobs processed

            #add workers to queue to process additional jobs
            while len(self.heapList) > 1 \
            and self.heapList[1][0] == self.jobtime \
            and len(self.jobs) > 0:
                self.worker = self.delMin()[1]  #remove top item from heap
                self.workers.append(self.worker) #add to worker queue
      
        return self.resultlist

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    pq = BinHeap()
    assigned_jobs = pq.build_pq(jobs, n_workers)

    for i, j in assigned_jobs:
        print(i, j)


if __name__ == "__main__":
    main()

#freeport_test.py
import unittest
from free_port import FreePort
 
def get_and_bind_freeport(*args):
    freeport = FreePort(start=4000, stop=4009)
    import time
    time.sleep(1)
    return freeport.port
 
class FreePortClassTest(unittest.TestCase):
    def test_one_port(self):
        freeport = FreePort(start=4000, stop=4000)
        self.assertEqual(freeport.port, 4000)
        freeport.release()
 
    def test_many_ports(self):
        freeport = FreePort(start=4000, stop=4000)
        self.assertEqual(freeport.port, 4000)
        freeport.release()
        freeport = FreePort(start=4000, stop=4000)
        self.assertEqual(freeport.port, 4000)
        freeport.release()
 
    def test_many_ports_conflict(self):
        def get_port():
            freeport = FreePort(start=4000, stop=4000)
            return freeport.port
 
        def run():
            self.assertEqual(get_port(), 4000)
 
        freeport = FreePort(start=4000, stop=4000)
        self.assertEqual(freeport.port, 4000)
 
        from multiprocessing import Process
        p = Process(target=run)
        p.start()
        p.join(0.1)
 
        self.assertTrue(p.is_alive(), 'the process should find it hard to acquire a free port')
 
        p.terminate()
        p.join()
 
        freeport.release()
 
    def test_multithread_race_condition(self):
        from multiprocessing.pool import ThreadPool
        jobs = 100
        def get_and_bind_freeport(*args):
            freeport = FreePort(start=4000, stop=4000 + jobs - 1)
            import time
            time.sleep(1)
            freeport.release() # needed because thread will not turn back the file descriptor
            return freeport.port
        p = ThreadPool(jobs)
        ports = p.map(get_and_bind_freeport, range(jobs))
        self.assertEqual(len(ports), len(set(ports)))
 
    def test_multiprocess_race_condition(self):
        from multiprocessing.pool import Pool
        p = Pool(10)
        ports = p.map(get_and_bind_freeport, range(10))
        self.assertEqual(len(ports), len(set(ports)))
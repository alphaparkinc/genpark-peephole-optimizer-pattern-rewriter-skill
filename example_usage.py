from client import PeepholeOptimizer

def main():
    print("=== Testing Peephole Pattern Rewriter ===")
    peep = PeepholeOptimizer()
    raw_ir = [
        ['t0', '*', 'r1', 2],
        ['t1', '+', 't0', 0],
        ['t2', '-', 'r3', 'r3']
    ]
    opt_ir = peep.optimize(raw_ir)
    print("Optimized IR:", opt_ir)
    assert opt_ir[0] == ['t0', 'SHL', 'r1', 1]
    assert opt_ir[1] == ['t1', 'MOV', 't0', None]
    assert opt_ir[2] == ['t2', 'CONST', 0, None]

    print("Peephole Optimizer verified successfully!")

if __name__ == '__main__':
    main()

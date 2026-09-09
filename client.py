class PeepholeOptimizer:
    """Peephole Pattern Matching Optimizer."""
    def optimize(self, insts):
        optimized = []
        for inst in insts:
            dest, op, s1, s2 = inst
            if op == '+' and s2 == 0:
                optimized.append([dest, 'MOV', s1, None])
            elif op == '*' and s2 == 1:
                optimized.append([dest, 'MOV', s1, None])
            elif op == '*' and s2 == 2:
                optimized.append([dest, 'SHL', s1, 1])
            elif op == '-' and s1 == s2:
                optimized.append([dest, 'CONST', 0, None])
            else:
                optimized.append(inst)

        final_insts = []
        for i in range(len(optimized)):
            if (i > 0 and
                optimized[i][1] == 'MOV' and
                optimized[i-1][0] == optimized[i][2] and
                optimized[i][0] == optimized[i-1][0]):
                continue
            final_insts.append(optimized[i])

        return final_insts

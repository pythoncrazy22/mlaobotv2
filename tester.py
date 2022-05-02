import oeispy as op
numbers = ['6','9','69']
num = ','.join(numbers)
result = op.resultEois(num)
sequence_oeis = op.topResult(result)
print(sequence_oeis)
print()
print(sequence_oeis["comment"][0])
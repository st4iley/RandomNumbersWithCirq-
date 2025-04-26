#Feito por mim Stanley Bayeux em 2025.
#Made by me, Stanley Bayeux, in 2025.
#Réalisé par moi, Stanley Bayeux, en 2025.


import cirq

qubits = {cirq.LineQubit(i) for i in range(3)} # 3 qubits

circuit = cirq.Circuit() 

for qubit in qubits:
    circuit.append(cirq.H(qubit)) #Superposicao

circuit.append(cirq.measure(*qubits, key = 'resultado')) 

simulator = cirq.Simulator()

resultado = simulator.run(circuit, repetitions=1) #simulador

bits = resultado.measurements['resultado'][0] 

numeros_aleatorios = sum(bit * (1 << i) for i, bit in enumerate(bits)) # cria numeros aleatorios

print({numeros_aleatorios})
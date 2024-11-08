import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(text):
    """
    Calcula la frecuencia de aparición de cada carácter en el texto.
    """
    return Counter(text)

def build_huffman_tree(frequencies):
    """
    Construye el árbol de Huffman a partir de las frecuencias de los caracteres.
    """
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Raíz del árbol

def generate_codes(node, current_code="", codes={}):
    """
    Genera los códigos de Huffman para cada carácter.
    """
    if node is None:
        return

    if node.char is not None:  # Nodo hoja
        codes[node.char] = current_code

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes

def encode_text(text, codes):
    """
    Codifica el texto utilizando los códigos de Huffman.
    """
    return ''.join(codes[char] for char in text)

def decode_text(encoded_text, root):
    """
    Decodifica el texto comprimido utilizando el árbol de Huffman.
    """
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        current_node = current_node.left if bit == '0' else current_node.right

        if current_node.char is not None:  # Nodo hoja
            decoded_text.append(current_node.char)
            current_node = root

    return ''.join(decoded_text)

# Función para análisis comparativo
def compression_analysis(original_text, encoded_text):
    original_size = len(original_text) * 8  # Tamaño en bits
    compressed_size = len(encoded_text)
    reduction_percentage = ((original_size - compressed_size) / original_size) * 100

    print(f"Tamaño original: {original_size} bits")
    print(f"Tamaño comprimido: {compressed_size} bits")
    print(f"Ahorro en espacio: {reduction_percentage:.2f}%")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        with open("arboles/archivo.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("El archivo no se encontró. Verifica la ruta.")
        text = ""



    # Cálculo de frecuencias y construcción del árbol de Huffman
    frequencies = calculate_frequencies(text)
    huffman_tree_root = build_huffman_tree(frequencies)
    codes = generate_codes(huffman_tree_root)

    # Codificación y decodificación
    encoded_text = encode_text(text, codes)
    decoded_text = decode_text(encoded_text, huffman_tree_root)

    # Verificación de que la decodificación sea correcta
    assert text == decoded_text, "El texto decodificado no coincide con el original."

    # Análisis comparativo
    compression_analysis(text, encoded_text)

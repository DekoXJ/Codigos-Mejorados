def AreaRect(baseRectangulo, alturaRectangulo):
    result = baseRectangulo * alturaRectangulo
    return result

def AreaTria(baseTriangulo, alturaTriangulo):
    resultado = 0.5 * baseTriangulo * alturaTriangulo
    return resultado

def main():
    baseRectangulo = 4
    alturaRectangulo = 6
    rect_area = AreaRect(baseRectangulo, alturaRectangulo)
    print("Área del rectángulo:", rect_area)

    baseTriangulo = 5
    alturaTriangulo = 8
    tri_area = AreaTria(baseTriangulo, alturaTriangulo)
    print("Área del triángulo:", tri_area)

main()
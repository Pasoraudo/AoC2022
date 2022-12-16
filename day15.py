from shapely import Polygon, LineString
import shapely.ops as so

with open('./data/day15.txt', 'r') as f:
    data = f.read().split('\n')

max_coor = 4000000
y_part1 = 2000000

min_xs, max_xs = [], []
poligonos = []
sensors_in_y_part1 = 0
for line in data:
    line2 = line.split(' ')
    sensor = (int(line2[2][2:-1]), int(line2[3][2:-1]))
    becon = (int(line2[8][2:-1]), int(line2[9][2:]))
    
    xs, ys = sensor[0], sensor[1]
    xv, yv = becon[0], becon[1]
    dis_x, dis_y = abs(xs - xv), abs(ys - yv)
    dis = dis_x + dis_y
    min_xs.append(xs - dis)
    max_xs.append(xs + dis)
    if ys == y_part1:
        sensors_in_y_part1 += 1
    dists = ( (dis, 0), (0, dis), (-dis, 0), (0, -dis) )
    poligonos.append(Polygon([(xs + x, ys + y) for x, y in dists]))
all_polygons = so.unary_union([i for i in poligonos])

# PARTE 1
line_part1 = LineString([(min(min_xs), y_part1), (max(max_xs), y_part1)])
part1_rec = all_polygons.intersection(line_part1)
xs, ys = part1_rec.coords.xy
part1 = abs(xs[0]) + abs(xs[1]) - sensors_in_y_part1
print('Problema 1:', part1)

# PARTE 2
mapa = Polygon([(0,0), (0, max_coor), (max_coor, max_coor), (max_coor, 0)])
all_polygons_recortado = mapa.intersection(all_polygons)
hole = mapa.difference(all_polygons_recortado)
xs, ys = hole.exterior.coords.xy
x, y = xs[1], ys[0] # es un poco raro pero da las coordenadas correctas
part2 = 4000000 * x + y
print('Problema 2:', part2)

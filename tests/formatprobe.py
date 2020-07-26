import sys
sys.path.insert(1, '../pymv')
from pymv import mv

mov = mv()
result = mov.probe('C:\\Users\\ryane\\Downloads\\Spider-Man.Into.the.Spider-Verse.2018.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.TrueHD.7.1.Atmos-FGT.mkv')
print(result.format.filename)
print(result.format.size_str())
duration = result.format.duration_obj()
print(duration)
print(duration.minute)
print(duration.second)
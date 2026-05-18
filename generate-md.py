def generate_minor_bands(major_band):
    major_start = (major_band - 1) * 4096
    minor_width = 256
    
    for minor in range(1, 17):
        minor_start = major_start + (minor - 1) * minor_width
        minor_end = minor_start + minor_width - 1
        
        print(f"- `{major_band:2}.{minor:<2} : {minor_start:<5} - {minor_end:<5}`")

for major_band in range(1, 17): 
    generate_minor_bands(major_band)
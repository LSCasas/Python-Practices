def celcius_to_fahrenheit(c):
    return (c * 9/5) + 32.0

celcius_presets = {
    "L1": 18,
    "L2": 20,
    "L3": 22,
    "L4": 23,
}

"""
Con dictionary comprehension
"""

fahrenheit_presets = {
 key: celcius_to_fahrenheit(value) for key, value in celcius_presets.items()

}

"""
Sin dicitionary comprenhension

for key, value in celcius_presets.items():
    fahrenheit_presets[key] = celcius_to_fahrenheit(value)

"""

print("En Celcius: ", celcius_presets)
print("En Fahrenheit: ", fahrenheit_presets)
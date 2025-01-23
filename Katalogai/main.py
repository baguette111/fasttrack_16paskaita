import pickle

# Example data for pajamos, islaidos, and minibiudzetas
pajamos = 1000
islaidos = 500
minibiudzetas = 500

# Saving data to the pickle file
with open("zurnalas.pkl", "wb") as file:
    pickle.dump(pajamos, file)
    pickle.dump(islaidos, file)
    pickle.dump(minibiudzetas, file)

try:
    with open("zurnalas.pkl", "wb") as file:
        pickle.dump(pajamos, file)
        pickle.dump(islaidos, file)
        pickle.dump(minibiudzetas, file)
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("zurnalas.pkl", "rb") as file:
        pajamos = pickle.load(file)
        islaidos = pickle.load(file)
        minibiudzetas = pickle.load(file)

    # Display the loaded data
    print("Pajamos:", pajamos)
    print("Islaidos:", islaidos)
    print("Minibiudzetas:", minibiudzetas)

except FileNotFoundError:
    print("The file 'zurnalas.pkl' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

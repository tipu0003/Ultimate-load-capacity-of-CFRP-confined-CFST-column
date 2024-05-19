import pickle
import tkinter as tk
from tkinter import ttk
import unicodeit
from PIL import Image, ImageTk
from tkinter import font

print(r'$H_{2}$')


# Function to load your model (dummy function)
# Function to load your model
def load_model():
    with open('BNNs_Pu.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


# Predict function to handle GUI input and show output
def predict():
    try:
        # Convert input values from strings to appropriate types (floats here)
        inputs = [float(entry.get()) for entry in entries]

        # Load your model
        model = load_model()

        # Make predictions using the model
        # Note: model.predict() generally expects a 2D array of inputs
        result = model.predict([inputs])[0]  # Get the first prediction from the results

        # Update the output label with the prediction result
        output_label.config(text=f'{unicodeit.replace('P_u')} (kN): {result:.2f}')
    except ValueError:
        # If there is an error in input conversion, notify the user
        output_label.config(text='Error: Please check input values.')
    except Exception as e:
        # Catch other potential errors from prediction or loading model
        output_label.config(text=f'Error: {str(e)}')


# Set up the main window
root = tk.Tk()
root.title('Load Prediction of CFRP-confined CFST columns')

# Define a style for the button
style = ttk.Style()
style.configure('TButton', background='blue', foreground='black', font=('Times New Roman', 12, 'bold'))

# function to convert to subscript
def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


# display subscript
print('f{}'.format(get_sub('co')))  # H₂SO₄

# Load and display an image
import os

# Specify your file path here
file_path = (r'C:\Users\rupes\OneDrive - charusat.edu.in\Upcoming Research Work\Collabration\China\New Papers and '
             r'Reports (18-01-2024)\ML Reports\Current\Topic 28 Revision\ML model\GUI\GUI_Image_1.png')
exists = os.path.exists(file_path)
print("File exists:", exists)

image = Image.open(r'C:\Users\rupes\OneDrive - charusat.edu.in\Upcoming Research Work\Collabration\China\New Papers '
                   r'and Reports (18-01-2024)\ML Reports\Current\Topic 28 Revision\ML model\GUI\GUI_Image_1.png')
# image = Image.open('GUI Image.jpg')
photo = ImageTk.PhotoImage(image)

# image_path = 'GUI Image.jpg'
# img = ImageTk.PhotoImage(Image.open(image_path))
# photo = tk.PhotoImage(file=image_path)
image_label = ttk.Label(root, image=photo)
image_label.grid(row=0, column=2, rowspan=10)

# Input labels and entries
# labels = ['e (mm)', 'H (mm)', 'f_co (MPa)', 'D_o (mm)', 't_s (mm)',
#           'f_y (MPa)', 't_f (mm)', 'E_f (MPa)', 'C_f (mm)']

# Input labels and entries
labels = [
    'e',  # No subscript needed
    'H',  # No subscript needed
    'f{}'.format(get_sub('co')),
    'D{}'.format(get_sub('o')),
    't{}'.format(get_sub('s')),
    'f{}'.format(get_sub('y')),
    't{}'.format(get_sub('f')),
    'E{}'.format(get_sub('f')),
    'C{}'.format(get_sub('f')),
]

entries = []
# Italic font setup
italic_font = font.Font(root, ('Times New Roman', 10, 'italic'))
for i, label in enumerate(labels):
    ttk.Label(root, text=label, font=italic_font).grid(row=i, column=0)
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

# Predict button
pu = 'P{}'.format(get_sub('u'))
predict_button = ttk.Button(root, text=f'Calculate {pu}', command=predict, style='TButton')
predict_button.grid(row=len(labels), column=0, columnspan=2)

# Output label
output_label = ttk.Label(root, text=f'{pu} (kN): ',font=('Times New Roman', 18, 'bold'))
output_label.grid(row=len(labels) + 1, column=0, columnspan=2)

# Run the main loop
root.mainloop()

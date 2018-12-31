import argparse
import SimpleITK as sitk


"""
This program checks that the given images have the correct aspect ratio for the 
various logos used by the windows installer created with the constructor program 
(https://github.com/conda/constructor/blob/master/CONSTRUCT.md).

Example: python check_logos.py --welcome_image rotatedSPIELogo.png --header_image spieLogo.png --icon_image logo.png

"""

welcome_image_aspect = 1.9146341463414633 # size (164,314)
header_image_aspect = 0.017543859649123 # size (150,57)
icon_image_aspect = 1.0 # size (256,256) 

def main(file_names, aspect_ratios):
    
    file_reader = sitk.ImageFileReader()
    for f_name, aspect in zip(file_names, aspect_ratios):
        file_reader.SetFileName(f_name)
        file_reader.ReadImageInformation()
        image_size = file_reader.GetSize()
        print(f_name + '\n\tExpected ratio: {0:.2f} , Actual ratio: {1:.2f}\n'.format(aspect, image_size[1]/image_size[0]))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check that aspect ratio of logos is close to what is expected for the ' +
                                                 'constructor program.\n(https://github.com/conda/constructor/blob/master/CONSTRUCT.md)')
    parser.add_argument('--welcome_image',
                        help='welcome image file name, expected aspect ratio is (1,{0:.2f})'.format(welcome_image_aspect))
    parser.add_argument('--header_image',
                        help='header image file name, expected aspect ratio is (1,{0:.2f})'.format(header_image_aspect))
    parser.add_argument('--icon_image',
                        help='icon image file name, expected aspect ratio is (1,{0:.2f})'.format(icon_image_aspect))
    
    args = parser.parse_args()
    # file name order must match the order in the aspect_ratios list.
    file_names = [args.welcome_image, args.header_image, args.icon_image]
    aspect_ratios = [welcome_image_aspect, header_image_aspect, icon_image_aspect]
    main(file_names, aspect_ratios)

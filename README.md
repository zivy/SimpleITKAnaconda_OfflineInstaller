# SimpleITK Anaconda Offline Installer

This material is used to create offline installers that include all relevant Anaconda packages for use with SimpleITK Jupyter notebooks.

We use the (conda) [constructor tool](https://github.com/conda/constructor) to create these installers. We cannot create all installers
on the same platform. Windows installers can only be created on a windows system (create_installers.bat). OSX and Linux installers can be created
on either of the two platforms (create_installers.sh).

When using an offline installer, all relevant packages are in the base environment, so the user only has to:
* On Windows: open the Jupyter notebook (under the start menu).
* On Linux/Mac, on the command line:
  ```
  source path_to_anaconda_dir/bin/activate
  jupyter notebook
  ```
Images used by the Windows installer have specific aspect ratios. The check_logos.py script prints the expected and actual aspect ratios.
Images will need to be resized if they are not close to the expected ratio, otherwise they are distorted (no need to worry about
the resampling to actual desired size, this is taken care of by the constructor).

# DeepLearning
Tinkering with Nvidia's "deep learning" implementation. Installation steps on
Manjaro Linux:

* Look up the latest and current proprietary Nvidia driver version:
*sudo mhwd-l; sudo mhwd -li*

* If not on latest, replace "440xx" with correct version:
*sudo mhwd -i pci video-nvidia-440xx*

* Install Nvidia packages, as described [here](https://wiki.archlinux.org/index.php/GPGPU#CUDA).
When prompted for an opencl-nvidia provider, select the one which matches
your Nvidia driver version: *sudo pacman -S cuda*

* Copy Nvidia's samples: *cd /opt/cuda/samples; sudo cp -R
samples samples_compiled; sudo chown -R <user> samples_compiled; sudo
chgrp -R <user> samples_compiled*

* Compile Nvidia's samples. If [this](https://github.com/NVIDIA/cuda-samples/issues/22)
error occurs, simply continue the build with "make -k":
*cd samples_compiled; make*

* Run a sample, ensure no errors: *bin/x86_64/linux/release/deviceQuery*

* Install boost and openblas-lapack: *sudo pacman -S boost;
yaourt -S openblas-lapack*

* Clone [this](https://github.com/asadalam/caffe) Manjaro-specific
Caffe fork, then follow the "Make" section of [these](http://caffe.berkeleyvision.org/installation.html)
instructions. Before running "make all", edit Makefile.config and
add 7.0 and 7.5 lines to "CUDA_ARCH", to reflect the RTX 2080's
[capabilities](https://developer.nvidia.com/cuda-gpus). Also undo
the change to shift to Python 3, also in Makefile.config

* Create a virtualenv for DIGITS: *mkvirtualenv -p /usr/bin/python2 digits*

* Make sure running in virtualenv: *workon digits*

* Execute these commands: *make pycaffe;
export CAFFE_ROOT=/home/sniper/Documents/Projects/NVIDIA/DIGITS/caffe*

* Edit requirements.txt, and replace the "pydot" line with "pydot3>=1.0.9".
Then run: *pip install -r requirements.txt;
pip install-r caffe/python/requirements.txt*

* Run: sudo ln -s /home/sniper/Documents/Projects/NVIDIA/DIGITS/caffe/distribute/lib/libcaffe.so.1.0.0 /usr/lib/libcaffe.so.1.0.0; 
export PYTHONPATH=/home/sniper/Documents/Projects/NVIDIA/DIGITS/caffe/python

* Run Digits from its base directory: *./digits-devserver*

* Won't run due to some error. I've spent untold hours on this, and
it still doesn't run. Need to draw the line somewhere.

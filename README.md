<!-- MARKDOWN LINKS & IMAGES -->

[status-icon]: https://img.shields.io/badge/status-active-success.svg
[project-url]: https://github.com/DamianTab/voice-gender-recognition
[issues-icon]: https://img.shields.io/github/issues/DamianTab/voice-gender-recognition.svg
[issues-url]: https://github.com/DamianTab/voice-gender-recognition/issues
[pulls-icon]: https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg
[pulls-url]: https://github.com/DamianTab/voice-gender-recognition/pulls
[license-icon]: https://shields.io/badge/license-Apache%202-blue.svg
[license-url]: /LICENSE
[author-url]: https://github.com/DamianTab

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./assets/logo.png" alt="Project logo"></a>
</p>


<h3 align="center">voice-gender-recognition</h3>

<div align="center">
  
  [![Status][status-icon]][project-url]
  [![GitHub Issues][issues-icon]][issues-url]
  [![GitHub Pull Requests][pulls-icon]][pulls-url]
  [![License][license-icon]][license-url]
</div>

---

<p align="center"> Program that checks your voice gender,
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Technologies](#technologies)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Deployment](#deployment)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

<br/>

## 🧐 About <a name = "about"></a>
Simply python project which handles voice recognition. It allows to recognize speaker gender.

More details are described in attached [report](report.pdf) (Polish language).

<br/>

## ⛏️ Technologies <a name = "technologies"></a>
- Python3

<br/>
  
## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will help you set up and run project on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

<br/>
  
### Prerequisites
What things you need to install the software and how to install them.

```
python v3
scipy
numpy
matplotlib
librosa
```
<br/>


The easiest way to install all libraries is to type:
```
pip3 install <package>
```
<br/>

### Running

To run code just type:
```
python3 main.py
```

<br/>


## 🎈 Usage <a name="usage"></a>
There are provided two similar algorithms. Algoritm `voice_recognition_HPS` is based on Harmonic Product Spectrum.

To run algorithm from `voice_recognition` inside your own code :

```
VoiceRecognitionAlgorithm().run(path + "/" + name)
```

To run algorithm from `voice_recognition_HPS` inside your own code :

```
main(path + "/" + name)
```


<br/>

## 🚀 Deployment <a name = "deployment"></a>
No available deployment method.

<br/>


<br/>

## ✍️ Authors <a name = "authors"></a>
- [@DamianTab][author-url]

<br/>

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

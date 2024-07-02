### 1. Install & activate

```bash
# Get the emsdk repo
git clone https://github.com/emscripten-core/emsdk.git

# Enter that directory
cd emsdk

# Fetch the latest version of the emsdk (not needed the first time you clone)
git pull

# Download and install the latest SDK tools.
./emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh
```

### 2. Build

prepare (https://github.com/61315/resynthesizer/issues/4):
```bash
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/engine.c -c -o engine.o
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/engineParams.c -c -o engineParams.o
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/glibProxy.c -c -o glibProxy.o
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/imageFormat.c -c -o imageFormat.o
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/imageSynth.c -c -o imageSynth.o
emcc -DSYNTH_LIB_ALONE -O3 -s resynthesizer/progress.c -c -o progress.o

emar rcs libresynthesizer.a engine.o engineParams.o glibProxy.o imageFormat.o imageSynth.o progress.o
```

And my build command:
```bash
emcc -O3 -flto -o interactive.html examples/painter_wasm.c -Iresynthesizer libresynthesizer.a -s USE_SDL=2 -s ALLOW_MEMORY_GROWTH=1 -s SINGLE_FILE
```

### 3. Extract 2nd `<script>` in html into `script2.js`

### 4. Modify the beginning of file (`var ROOT` is declared in `iframe.py`):

```js
var ARGUMENT = 'upload.ppm'
var LINK = '/file=' + ROOT + '/' + ARGUMENT

```

+ fin `arguments_ = [],` and replace with `arguments_ = [ARGUMENT],`

And modify the ending before running block:
```js
// Correct usage inside an async function
async function loadFile(url) {
    try {
        const timestamp = new Date().getTime();
        const response = await fetch(url + "?" + timestamp);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const blob = await response.blob();
        // Handle the loaded file, e.g., pass it to Emscripten
        await handleFile(blob);
    } catch (error) {
        console.error('Error fetching file:', error);
    }
}

async function handleFile(blob) {
    // Example: Using the fetched blob
    FS.writeFile(ARGUMENT, new Uint8Array(await blob.arrayBuffer()));
    console.log(ARGUMENT + ' saved')
}
```

+ wrap running block into async instant called function:
```js
(async () => {
    try {
        await loadFile(LINK);

        // running here

} catch (error) {
    console.error('Error in IIFE:', error);
}
})();
```

global var `shouldRunNow` should stay outside

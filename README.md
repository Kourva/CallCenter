<div align="center">
<table align="center">
  <tbody align="center">
    <tr align="center">
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/e259e98e-0cdb-4156-8101-a606416ea76b" width="80px;" alt="Azerbaijan"/>
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/40f63c88-3e0f-4f28-ae2b-95f5b0f60d67" width="80px;" alt="India"/>
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/3cd2858f-25db-4ac1-bc06-cc84162e83bb" width="80px;" alt="Iran"/>
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/78f4128c-09e2-49b7-819c-5c840733af67" width="80px;" alt="Japan"/>
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/58c8da1e-d019-4848-9708-c3a4f5b5c799" width="80px;" alt="Turkey"/>
        <img src="https://github.com/Kourva/CallCenter/assets/118578799/1ee41a11-3c76-4e36-9a7a-2b4e0afe7504" width="80px;" alt="Afghanistan"/>
    </tr>
  </tbody>
</table>
  <h3><b>Call Center</b></h3>
  <p>GUI TTS app made in Flet</p>
</div>

<div align="center">
    <img align="center" src="https://github.com/Kourva/CallCenter/assets/118578799/72e45da1-af6b-4197-9ea8-e9857faa15a1"/>
</div>

# Installation
1. **Clone CallCenter repository**:
    ```bash
    git clone https://github.com/Kourva/CallCenter
    ```
2. **Nevigate to source file**:
    ```bash
    cd CallCenter
    ```
3. **Create virtual environment**:
    ```bash
    virtualenv venv && source venv/bin/activate
    ```
    > Note that you may need to execute different activate file based on your shell
4. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Run the app using flet**:
    ```bash
    flet run main.py
    ```

# Flet Issue
If you got this error on flet: libmpv.so.1 not found (when libmpv is already installed):
```bash
 sudo ln -s /usr/lib/libmpv.so /usr/lib/libmpv.so.1
```

# Thanks to lazypy.ro for API
Check out [**lazypy**](https://lazypy.ro) for more tts voices...

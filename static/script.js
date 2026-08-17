const sourceText = document.getElementById("sourceText");
const sourceLang = document.getElementById("sourceLang");
const targetLang = document.getElementById("targetLang");
const translateButton = document.getElementById("translateButton");
const clearButton = document.getElementById("clearButton");
const copyButton = document.getElementById("copyButton");
const ttsButton = document.getElementById("ttsButton");
const translationResult = document.getElementById("translationResult");
const statusMessage = document.getElementById("statusMessage");

function setStatus(message, isError = false, isLoading = false) {
    statusMessage.textContent = message;
    statusMessage.classList.toggle("error", isError);
    statusMessage.classList.toggle("loading", isLoading);
}

function setResult(text) {
    translationResult.textContent = text;
}

function setLoading(isLoading) {
    translateButton.disabled = isLoading;
    if (isLoading) {
        setStatus("Translating... Please wait.", false, true);
    } else if (!statusMessage.classList.contains("error")) {
        setStatus("");
    }
}

async function translateText() {
    const text = sourceText.value.trim();
    const source = sourceLang.value;
    const target = targetLang.value;

    if (!text) {
        setStatus("Please enter text to translate.", true);
        return;
    }

    setResult("");
    setLoading(true);

    try {
        const response = await fetch("/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text,
                source_lang: source,
                target_lang: target,
            }),
        });

        const data = await response.json();
        setLoading(false);

        if (!response.ok) {
            setStatus(data.error || "Translation failed.", true);
            return;
        }

        setResult(data.translatedText);
        setStatus("Translation completed successfully.");
    } catch (error) {
        setLoading(false);
        setStatus("Unable to reach the server. Make sure LibreTranslate is running.", true);
        console.error(error);
    }
}

function copyTranslation() {
    const text = translationResult.textContent.trim();
    if (!text) {
        setStatus("No translated text available to copy.", true);
        return;
    }

    if (!navigator.clipboard) {
        setStatus("Clipboard is not supported in this browser.", true);
        return;
    }

    navigator.clipboard.writeText(text).then(
        () => setStatus("Copied translated text to clipboard."),
        () => setStatus("Copy failed. Please try again.", true)
    );
}

function speakTranslation() {
    const text = translationResult.textContent.trim();
    if (!text) {
        setStatus("No translated text available for speech.", true);
        return;
    }

    if (!window.speechSynthesis) {
        setStatus("Text-to-speech is not supported in this browser.", true);
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = targetLang.value;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
}

function clearForm() {
    sourceText.value = "";
    setResult("");
    setStatus("");
    sourceLang.value = "auto";
}

translateButton.addEventListener("click", translateText);
clearButton.addEventListener("click", clearForm);
copyButton.addEventListener("click", copyTranslation);
ttsButton.addEventListener("click", speakTranslation);

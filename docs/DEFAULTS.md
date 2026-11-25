# Nexus AI — Default Configuration

## AI Settings

```ini
AI_PROVIDER=offline
OPENROUTER_MODEL=openrouter/free
AI_DAILY_REQUEST_LIMIT=40
AI_MAX_TOKENS=500
```

## Voice Settings

```ini
WAKE_WORD=hey nexus
VOICE_LANGUAGE=en-US
```

## Camera Settings

```ini
CAMERA_WIDTH=640
CAMERA_HEIGHT=480
CAMERA_FPS=24
```

## Performance Settings

```ini
PERFORMANCE_PROFILE=auto
GESTURE_COOLDOWN_MS=800
```

## Local Model Paths

Development paths relative to the repository root:

```ini
VOSK_MODEL_PATH=models/vosk
HAND_MODEL_PATH=models/mediapipe/hand_landmarker.task
FACE_MODEL_PATH=models/mediapipe/face_landmarker.task
POSE_MODEL_PATH=models/mediapipe/pose_landmarker_lite.task
```

Production model paths must be explicitly resolved using the application's resource or application data directories. Never rely on the current working directory.

## Security Requirements

- Offline mode is enabled by default.
- OpenRouter integration is optional.
- API keys must never be stored in source code, configuration files, Git or installers.
- Store API keys securely using Windows Credential Manager through the Rust keyring integration.
- The daily request limit is enforced by Nexus AI and does not guarantee the provider's available quota.

## Implementation Plan

- Phase 1: Convert documented settings into typed Rust configuration defaults.
- Phase 2: Persist and load user configuration overrides.
- Validate user-provided configuration before applying it.
- Restore documented defaults when the user resets application settings.

## External Resources

OpenRouter API keys: https://openrouter.ai/settings/keys

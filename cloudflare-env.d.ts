declare namespace Cloudflare {
  interface Env {
    DB?: D1Database;
    BUCKET?: R2Bucket;
    PRIVACY_CONTACT_EMAIL?: string;
    FIREBASE_API_KEY?: string;
    FIREBASE_PROJECT_ID?: string;
  }
}

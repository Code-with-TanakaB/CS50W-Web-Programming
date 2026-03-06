/*
 * api.js — A simple REST API built with Node.js and Express
 *
 * This server exposes a small in-memory "notes" resource so you can
 * practise making fetch() calls from storage.html (or any front-end).
 *
 * Endpoints
 * ---------
 *  GET    /api/notes          → return all notes
 *  GET    /api/notes/:id      → return a single note by id
 *  POST   /api/notes          → create a new note  (body: { title, body })
 *  PUT    /api/notes/:id      → update a note      (body: { title?, body? })
 *  DELETE /api/notes/:id      → delete a note
 *
 * Run with:
 *   npm install express        (first time only)
 *   node api.js
 *
 * The server listens on http://localhost:3000
 */

// ── Dependencies ──────────────────────────────────────────────────────────────
const express = require("express");
const app     = express();

// Parse incoming JSON request bodies automatically
app.use(express.json());

// Serve all HTML/JS/CSS files in this folder at the root URL
// e.g. http://localhost:3000/currency.html
app.use(express.static(__dirname));

// Allow the browser to call this API from a different origin (CORS)
app.use(function(req, res, next) {
    res.setHeader("Access-Control-Allow-Origin",  "*");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
    // Respond to pre-flight OPTIONS requests immediately
    if (req.method === "OPTIONS") return res.sendStatus(204);
    next();
});

// ── In-Memory Data Store ──────────────────────────────────────────────────────
/*
 * Notes are stored in a plain array while the server is running.
 * Restarting the server resets the data (no database needed for this demo).
 * Each note has: { id, title, body, createdAt }
 */
let notes = [];

// Simple auto-incrementing id counter
let nextId = 1;

// ── Helper ────────────────────────────────────────────────────────────────────

/**
 * Finds a note by id and returns it, or undefined if not found.
 * @param {number} id - The numeric id to search for
 */
function findNote(id) {
    return notes.find(note => note.id === id);
}

// ── Routes ────────────────────────────────────────────────────────────────────

/* GET /api/notes
 * Returns the full list of notes as JSON.
 * Example response: [{ id: 1, title: "Hello", body: "World", createdAt: "..." }]
 */
app.get("/api/notes", function(req, res) {
    res.json(notes);
});

/* GET /api/notes/:id
 * Returns a single note by its numeric id.
 * Responds with 404 if the id doesn't exist.
 */
app.get("/api/notes/:id", function(req, res) {
    const note = findNote(parseInt(req.params.id));

    if (!note) {
        // 404 Not Found — no note with this id
        return res.status(404).json({ error: "Note not found." });
    }

    res.json(note);
});

/* POST /api/notes
 * Creates a new note from the JSON body.
 * Required fields: title
 * Optional fields: body
 * Responds with 201 Created and the new note object.
 */
app.post("/api/notes", function(req, res) {
    const { title, body } = req.body;

    // Validate: title is required
    if (!title || title.trim() === "") {
        return res.status(400).json({ error: "Field 'title' is required." });
    }

    // Build the new note object
    const note = {
        id:        nextId++,            // assign then increment the counter
        title:     title.trim(),
        body:      (body || "").trim(),
        createdAt: new Date().toISOString()
    };

    // Append to the in-memory store
    notes.push(note);

    // 201 Created — return the newly created note
    res.status(201).json(note);
});

/* PUT /api/notes/:id
 * Updates an existing note's title and/or body.
 * Only the fields included in the request body are changed.
 * Responds with the updated note, or 404 if not found.
 */
app.put("/api/notes/:id", function(req, res) {
    const note = findNote(parseInt(req.params.id));

    if (!note) {
        return res.status(404).json({ error: "Note not found." });
    }

    const { title, body } = req.body;

    // Only overwrite a field if the caller actually sent it
    if (title !== undefined) note.title = title.trim();
    if (body  !== undefined) note.body  = body.trim();

    res.json(note);
});

/* DELETE /api/notes/:id
 * Removes a note by id.
 * Responds with 204 No Content on success, or 404 if not found.
 */
app.delete("/api/notes/:id", function(req, res) {
    const id    = parseInt(req.params.id);
    const index = notes.findIndex(note => note.id === id);

    if (index === -1) {
        return res.status(404).json({ error: "Note not found." });
    }

    // Remove the note at the found index (splice mutates the array in place)
    notes.splice(index, 1);

    // 204 No Content — success, nothing to return
    res.sendStatus(204);
});

// ── Start Server ──────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;

app.listen(PORT, function() {
    console.log(`API server running at http://localhost:${PORT}`);
    console.log("Available endpoints:");
    console.log("  GET    /api/notes");
    console.log("  GET    /api/notes/:id");
    console.log("  POST   /api/notes    { title, body }");
    console.log("  PUT    /api/notes/:id { title?, body? }");
    console.log("  DELETE /api/notes/:id");
});

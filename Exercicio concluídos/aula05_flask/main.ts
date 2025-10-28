// Define a estrutura de dados para o usuário
interface User {
    id: number;
    name: string;
}

// Utilitários de DOM e Formatação
const $ = (id: string): HTMLInputElement => document.getElementById(id) as HTMLInputElement;

const jsonPretty = (obj: any): string => 
    `<pre style="white-space:pre-wrap; margin:0">${escapeHtml(JSON.stringify(obj, null, 2))}</pre>`;

const escapeHtml = (s: string): string => 
    String(s)
        .replaceAll("&", "&amp;").replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#039;");

// IDs das mensagens de feedback
const MSG_IDS: string[] = ["listMsg", "getMsg", "createMsg", "updateMsg", "deleteMsg"];

function base(): string {
    let u = $("baseUrl").value.trim();
    if (u.endsWith("/")) u = u.slice(0, -1);
    return u;
}

function resetUI(activeMsgId?: string): void {
    for (const id of MSG_IDS) {
        const el = document.getElementById(id) as HTMLSpanElement | null;
        if (!el) continue;
        
        // Limpa a mensagem ativa, se especificada, ou todas
        if (!activeMsgId || id === activeMsgId) {
            el.className = "msg";
            el.textContent = "";
        }
    }
    document.getElementById("output")!.innerHTML = "";
}

interface ApiResponse {
    ok: boolean;
    status: number;
    data: any;
}

async function api(path: string, opts: RequestInit = {}): Promise<ApiResponse> {
    const url = `${base()}${path}`;
    
    // Define cabeçalhos padrão para JSON
    const headers = { 
        "Content-Type": "application/json; charset=utf-8", 
        ...(opts.headers as Record<string, string> || {}) 
    };

    try {
        const res = await fetch(url, { headers, ...opts });
        const text = await res.text();
        let data: any = null;
        
        try { 
            data = text ? JSON.parse(text) : null; 
        } catch { 
            data = text; 
        }

        return { ok: res.ok, status: res.status, data };

    } catch (e) {
        // Erro de rede (CORS, servidor inalcançável, etc.)
        return { ok: false, status: 0, data: { message: `Erro de rede: ${e instanceof Error ? e.message : String(e)}` } };
    }
}

function showOut(title: string, payload: any, ok: boolean = true): void {
    const out = document.getElementById("output")!;
    const klass = ok ? "ok" : "err";
    out.innerHTML = `<div class="${klass}" style="margin-bottom:8px">${escapeHtml(title)}</div>${jsonPretty(payload ?? {})}`;
}

function setMsg(id: string, msg: string, ok: boolean = true): void {
    const el = document.getElementById(id) as HTMLSpanElement;
    el.className = `msg ${ok ? "ok" : "err"}`;
    el.textContent = msg || "";
}

// Funções de Ação do CRUD (exportadas para serem chamadas do HTML)

export function clearOutput(manual: boolean = false): void {
    document.getElementById("output")!.innerHTML = manual ? "Saída limpa." : "";
    resetUI();
}

export async function ping(): Promise<void> {
    resetUI("listMsg");
    try {
        const r = await api("/users");
        const statusMsg = r.ok ? "Conectado! ✅" : `Falhou (${r.status})`;
        setMsg("listMsg", statusMsg, r.ok);
        showOut("GET /users (ping)", r, r.ok);
    } catch (e) {
        setMsg("listMsg", "Erro de conexão", false);
        showOut("Erro", { message: String(e) }, false);
    }
}

export async function listUsers(): Promise<void> {
    resetUI("listMsg");
    const r = await api("/users");
    const statusMsg = r.ok ? "OK" : `Erro ${r.status}`;
    setMsg("listMsg", statusMsg, r.ok);
    showOut("GET /users", r, r.ok);
}

export async function getUser(): Promise<void> {
    resetUI("getMsg");
    const idValue = $("getId").value;
    const id = Number(idValue);
    
    if (!idValue || isNaN(id) || id <= 0) {
        return setMsg("getMsg", "Informe um ID válido.", false);
    }

    const r = await api(`/users/${id}`);
    const statusMsg = r.ok ? "OK" : `Erro ${r.status}`;
    setMsg("getMsg", statusMsg, r.ok);
    showOut(`GET /users/${id}`, r, r.ok);
}

export async function createUser(): Promise<void> {
    resetUI("createMsg");
    const idValue = $("createId").value;
    const name = $("createName").value.trim();
    const id = Number(idValue);

    if (!idValue || isNaN(id) || id <= 0 || !name) {
        return setMsg("createMsg", "Preencha ID (número) e Nome.", false);
    }

    const newUser: User = { id, name };

    const r = await api("/users", {
        method: "POST",
        body: JSON.stringify(newUser)
    });
    
    const statusMsg = r.ok ? "Criado!" : `Erro ${r.status}`;
    setMsg("createMsg", statusMsg, r.ok);
    showOut("POST /users", r, r.ok);
}

export async function updateUser(): Promise<void> {
    resetUI("updateMsg");
    const idValue = $("updateId").value;
    const name = $("updateName").value.trim();
    const id = Number(idValue);

    if (!idValue || isNaN(id) || id <= 0 || !name) {
        return setMsg("updateMsg", "Preencha ID (número alvo) e Nome (novo).", false);
    }
    
    const updateData: Partial<User> = { name };
    // A API pode exigir o ID no corpo, dependendo da implementação, mas o PUT é geralmente usado com o ID na URL.
    // Incluí o ID para compatibilidade com a implementação original (JSON.stringify({ id, name })), mas tipamos a requisição corretamente.
    
    const r = await api(`/users/${id}`, {
        method: "PUT",
        body: JSON.stringify({ id, name }) 
    });
    
    const statusMsg = r.ok ? "Atualizado!" : `Erro ${r.status}`;
    setMsg("updateMsg", statusMsg, r.ok);
    showOut(`PUT /users/${id}`, r, r.ok);
}

export async function deleteUser(): Promise<void> {
    resetUI("deleteMsg");
    const idValue = $("deleteId").value;
    const id = Number(idValue);

    if (!idValue || isNaN(id) || id <= 0) {
        return setMsg("deleteMsg", "Informe um ID válido.", false);
    }

    const r = await api(`/users/${id}`, { method: "DELETE" });
    const statusMsg = r.ok ? "Removido!" : `Erro ${r.status}`;
    setMsg("deleteMsg", statusMsg, r.ok);
    showOut(`DELETE /users/${id}`, r, r.ok);
}

// ***************
// Vinculação global para uso no HTML
// ***************
// Em um ambiente de módulo, você precisa anexar as funções ao objeto global (window)
// para que o HTML (onclick="ping()") possa encontrá-las.

declare global {
    interface Window {
        ping: typeof ping;
        listUsers: typeof listUsers;
        getUser: typeof getUser;
        createUser: typeof createUser;
        updateUser: typeof updateUser;
        deleteUser: typeof deleteUser;
        clearOutput: typeof clearOutput;
    }
}

window.ping = ping;
window.listUsers = listUsers;
window.getUser = getUser;
window.createUser = createUser;
window.updateUser = updateUser;
window.deleteUser = deleteUser;
window.clearOutput = clearOutput;
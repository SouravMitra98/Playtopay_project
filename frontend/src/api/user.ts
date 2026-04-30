export async function api<T>(url: string, options?: RequestInit): Promise<T> {
    const res = await fetch(url, options);

    if(!res.ok){
        throw new Error(`API request error: ${res.status} ${res.statusText}`);
    }
    const data: T = await res.json();
    return data;
}
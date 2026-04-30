export interface merchant {
    id: number;
    name: string;
}

export async function getmerchant(): Promise<merchant[]> {
    const res = await fetch("/api/v1/merchant");
    return res.json();
}
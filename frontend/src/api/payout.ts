import { api } from "./user";

export interface PayoutPayLoad{
    amount: number;
    bank_ac_id: string;
}

export interface PayoutRes{
    id: number;
    status: string;
}

export const pay = (data: PayoutPayLoad): Promise<PayoutRes> =>{
    console.log("API PAYLOAD:", data);
    return api<PayoutRes>("http://127.0.0.1:8000/api/v1/payouts/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Idempotency-Key": crypto.randomUUID(),
        },
        body: JSON.stringify(data),
    });
};
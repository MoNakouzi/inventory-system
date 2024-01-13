import { NextResponse } from "next/server";

export async function GET() {
    return NextResponse.json({
        "hello world": "how are you"
    });
}

export async function POST() {
    return NextResponse.json({
        "post request": "success"
    })
}
# DeVloped By AbdeeLkarim Amiri
# Updated for OB52 - version 1.120.1 (2019119621)
# Memory optimized for 24/7 hosting
import requests
import os
import psutil
import sys
import jwt
import pickle
import json
import binascii
import time
import urllib3
import xKEys
import base64
import datetime
import re
import socket
import threading
import http.client
import ssl
import gzip
import asyncio
import gc

from io import BytesIO
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from threading import Thread
from cfonts import render, say
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def G_AccEss(U, P):
    UrL = "https://100067.connect.garena.com/oauth/guest/token/grant"
    HE = {
        "Host": "100067.connect.garena.com",
        "User-Agent": Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close",
    }
    dT = {
        "uid": f"{U}",
        "password": f"{P}",
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067",
    }
    try:
        R = requests.post(UrL, headers=HE, data=dT, timeout=15)
        if R.status_code == 200:
            return R.json()["access_token"], R.json()["open_id"]
        else:
            print(R.json())
            return None
    except Exception as e:
        print(e)
        return None


def MajorLoGin(PyL):
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection("loginbp.ggblueshark.com", context=context)
    headers = {
        "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB52",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
        "Host": "loginbp.ggblueshark.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    try:
        conn.request("POST", "/MajorLogin", body=PyL, headers=headers)
        response = conn.getresponse()
        raw_data = response.read()
        if response.getheader("Content-Encoding") == "gzip":
            with gzip.GzipFile(fileobj=BytesIO(raw_data)) as f:
                raw_data = f.read()
        TexT = raw_data.decode(errors="ignore")
        if "BR_PLATFORM_INVALID_OPENID" in TexT or "BR_GOP_TOKEN_AUTH_FAILED" in TexT:
            sys.exit()
        return raw_data.hex() if response.status in [200, 201] else None
    finally:
        conn.close()


Thread(target=AuTo_ResTartinG, daemon=True).start()


async def periodic_gc():
    while True:
        await asyncio.sleep(10 * 60)
        gc.collect()
        print(" - [GC] Forced garbage collection done")


class FF_CLient:
    def __init__(self, U, P, forced_target=None):
        self.empty_count = 0
        self.reader = None
        self.writer = None
        self.reader2 = None
        self.writer2 = None
        self.forced_target = forced_target
        self.U = U
        self.P = P

    async def run(self):
        await self.Get_FiNal_ToKen_0115(self.U, self.P)

    async def STarT(self, JwT_ToKen, AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid):
        R = asyncio.Event()
        task1 = asyncio.create_task(
            self.ChaT(self.JwT_ToKen, self.AutH_ToKen, ip, port, key, iv, bot_uid, R)
        )
        await R.wait()
        task2 = asyncio.create_task(
            self.OnLinE(self.JwT_ToKen, self.AutH_ToKen, ip2, port2, key, iv, bot_uid)
        )
        try:
            await asyncio.gather(task1)
        finally:
            task2.cancel()
            try:
                await task2
            except asyncio.CancelledError:
                pass
            await self._close_writers()

    async def _close_writers(self):
        for attr in ("writer", "writer2"):
            w = getattr(self, attr, None)
            if w:
                try:
                    w.close()
                    await w.wait_closed()
                except Exception:
                    pass
                setattr(self, attr, None)
        for attr in ("reader", "reader2"):
            setattr(self, attr, None)
        gc.collect()

    async def sF(self):
        await self._close_writers()

    async def OnLinE(self, Token, tok, host2, port2, key, iv, bot_uid):
        T = "ar"
        global writer, writer2, TarGeT, sQ, Nm
        while True:
            try:
                self.reader2, self.writer2 = await asyncio.open_connection(host2, int(port2))
                self.writer2.write(bytes.fromhex(tok))
                await self.writer2.drain()
                while True:
                    try:
                        data = await self.reader2.read(2048)
                        if not data:
                            break
                        data = None
                    except asyncio.CancelledError:
                        raise
                    except Exception:
                        await asyncio.sleep(2)
                        break
            except asyncio.CancelledError:
                raise
            except Exception:
                await asyncio.sleep(3)

    async def ChaT(self, Token, tok, host, port, key, iv, bot_uid, R):
        T = "fr"
        print(bot_uid)
        global writer, writer2, TarGeT, sQ, Nm
        while True:
            try:
                self.reader, self.writer = await asyncio.open_connection(host, int(port))
                self.writer.write(bytes.fromhex(tok))
                await self.writer.drain()
                self.writer.write(GLobaL(T, key, iv))
                await self.writer.drain()
                R.set()
                while True:
                    try:
                        data = await self.reader.read(2048)
                        if not data:
                            break
                        if data.hex().startswith("1200") and b"SecretCode" in data:
                            U = json.loads(DeCode_PackEt(data.hex()[10:]))
                            U2 = json.loads(DeCode_PackEt(data.hex()[36:]))
                            Uu = json.loads(U["5"]["data"]["8"]["data"])

                            Nm = U2["9"]["data"]["1"]["data"]
                            if self.forced_target:
                                try:
                                    TarGeT = int(self.forced_target)
                                except Exception:
                                    TarGeT = int(Uu.get("GroupID", 0))
                            else:
                                TarGeT = int(Uu["GroupID"])

                            sQ = Uu["SecretCode"]
                            rQ = Uu.get("RecruitCode")

                            U = None
                            U2 = None
                            Uu = None

                            self.writer.write(RedZed_3alamyia_Chat(TarGeT, sQ, key, iv))
                            await self.writer.drain()

                            msg_part1 = (
                                "-HELLO I AM fuck   !\n\n"
                                "SUBSCRIBE ME ON YOUTUBE  OR BE BANNED \n\n"
                                "SBPRIME HERE : "
                            )
                            msg_part2 = "@axromjanyt !! \n\n"
                            msg_part3 = (
                                "telegram team channel : @axemoteserver \n\n"
                                "DEV Telegram username : @axromjanhissain"
                            )

                            full_msg = (
                                "[FF0000][B][C]"
                                + xMsGFixinG(msg_part1)
                                + "[00FF00]"
                                + xMsGFixinG(msg_part2)
                                + "[FFFF00]"
                                + xMsGFixinG(msg_part3)
                            )

                            self.writer.write(RedZed_SendMsg(full_msg, TarGeT, bot_uid, key, iv))
                            await self.writer.drain()

                            try:
                                self.writer2.write(RedZed_SendInv(bot_uid, TarGeT, key, iv))
                                await self.writer2.drain()
                            except Exception:
                                pass

                            try:
                                self.writer.write(quit_caht_redzed(TarGeT, key, iv))
                                await self.writer.drain()
                            except Exception:
                                pass

                            print("With => {}".format(bot_uid), "To => {}".format(TarGeT))
                            data = None
                            return
                        else:
                            data = None

                    except asyncio.CancelledError:
                        raise
                    except Exception:
                        await asyncio.sleep(2)
                        break
            except asyncio.CancelledError:
                raise
            except Exception:
                await asyncio.sleep(3)

    def GeT_Key_Iv(self, serialized_data):
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)
        timestamp, key, iv = my_message.field21, my_message.field22, my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp, key, iv

    def _GeT_LoGin_PorTs_sync(self, JwT_ToKen, PayLoad):
        UrL = "https://clientbp.ggwhitehawk.com/GetLoginData"
        HeadErs = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {JwT_ToKen}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB52",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)",
            "Host": "clientbp.ggwhitehawk.com",
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            Res = requests.post(UrL, headers=HeadErs, data=PayLoad, verify=False)
            BesTo_data = json.loads(DeCode_PackEt(Res.content.hex()))
            address, address2 = BesTo_data["32"]["data"], BesTo_data["14"]["data"]
            ip, ip2 = address[: len(address) - 6], address2[: len(address) - 6]
            port, port2 = address[len(address) - 5 :], address2[len(address2) - 5 :]
            return ip, port, ip2, port2
        except requests.RequestException as e:
            print(f" - Bad Requests !")
        print(" - Failed To GeT PorTs !")
        return None, None, None, None

    async def ToKen_GeneRaTe(self, U, P):
        try:
            if U and P:
                result = await asyncio.to_thread(G_AccEss, U, P)
                if not result:
                    return None
                self.PLaFTrom = 4
                self.A, self.O = result
                self.Version, self.V = "2019119621", "1.120.1"
                PyL = {
                    3: str(datetime.now())[:-7],
                    4: "free fire",
                    5: 1,
                    7: self.V,
                    8: "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)",
                    9: "Handheld",
                    10: "Verizon Wireless",
                    11: "WIFI",
                    12: 1280,
                    13: 960,
                    14: "240",
                    15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",
                    16: 5951,
                    17: "Adreno (TM) 640",
                    18: "OpenGL ES 3.0",
                    19: "Google|0fc0e446-ca27-4faa-824a-d40d77767de9",
                    20: "20.171.73.202",
                    21: "fr",
                    22: self.O,
                    23: self.PLaFTrom,
                    24: "Handheld",
                    25: "google G011A",
                    29: self.A,
                    30: 1,
                    41: "Verizon Wireless",
                    42: "WIFI",
                    57: "1ac4b80ecf0478a44203bf8fac6120f5",
                    60: 32966,
                    61: 29779,
                    62: 2479,
                    63: 914,
                    64: 31176,
                    65: 32966,
                    66: 31176,
                    67: 32966,
                    70: 4,
                    73: 2,
                    74: "/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/lib/arm",
                    76: 1,
                    77: "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/base.apk",
                    78: 6,
                    79: 1,
                    81: "32",
                    83: self.Version,
                    86: "OpenGLES2",
                    87: 255,
                    88: self.PLaFTrom,
                    89: "J\u0003FD\u0004\r_UH\u0003\u000b\u0016_\u0003D^J>\u000fWT\u0000\\=\nQ_;\u0000\r;Z\u0005a",
                    90: "Phoenix",
                    91: "AZ",
                    92: 10214,
                    93: "3rd_party",
                    94: "KqsHT7gtKWkK0gY/HwmdwXIhSiz4fQldX3YjZeK86XBTthKAf1bW4Vsz6Di0S8vqr0Jc4HX3TMQ8KaUU3GeVvYzWF9I=",
                    95: 111207,
                    97: 1,
                    98: 1,
                    99: f"{self.PLaFTrom}",
                    100: f"{self.PLaFTrom}",
                }
            try:
                PyL_hex = CrEaTe_ProTo(PyL).hex()
                PyL = None
                print(PyL_hex)
                PaYload = bytes.fromhex(EnC_AEs(PyL_hex))
                PyL_hex = None
            except:
                ResTarTinG()
                return None
            ResPonse = await asyncio.to_thread(MajorLoGin, PaYload)
            if ResPonse:
                BesTo_data = json.loads(DeCode_PackEt(ResPonse))
                print(BesTo_data)
                bot_uid = BesTo_data["1"]["data"]
                JwT_ToKen = BesTo_data["8"]["data"]
                BesTo_data = None
                combined_timestamp, key, iv = self.GeT_Key_Iv(bytes.fromhex(ResPonse))
                ResPonse = None
                ip, port, ip2, port2 = await asyncio.to_thread(
                    self._GeT_LoGin_PorTs_sync, JwT_ToKen, PaYload
                )
                PaYload = None
                return (
                    JwT_ToKen,
                    key,
                    iv,
                    combined_timestamp,
                    ip,
                    port,
                    ip2,
                    port2,
                    bot_uid,
                )
        except Exception as e:
            print("From Token Generate ", e)
            return None

    async def Get_FiNal_ToKen_0115(self, U, P):
        result = await self.ToKen_GeneRaTe(U, P)
        if not result:
            return
        token, key, iv, Timestamp, ip, port, ip2, port2, bot_uid = result
        self.JwT_ToKen = token
        try:
            AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            AccounT_Uid = AfTer_DeC_JwT.get("account_id")
            self.Nm = AfTer_DeC_JwT.get("nickname")
            self.H, self.M, self.S = GeT_Time(AfTer_DeC_JwT.get("exp"))
            self.Vr = AfTer_DeC_JwT.get("release_version")
            EncoDed_AccounT = hex(AccounT_Uid)[2:]
            HeX_VaLue = DecodE_HeX(Timestamp)
            TimE_HEx = HeX_VaLue
            JwT_ToKen_ = token.encode().hex()
            AfTer_DeC_JwT = None
        except Exception as e:
            print(f" - Error In ToKen : {e}")
            return
        try:
            Header = hex(len(EnC_PacKeT(JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(EncoDed_AccounT)
            pad = "00000000"
            if length == 9:
                pad = "0000000"
            elif length == 8:
                pad = "00000000"
            elif length == 10:
                pad = "000000"
            elif length == 7:
                pad = "000000000"
            else:
                print("Unexpected length encountered")
            Header = f"0115{pad}{EncoDed_AccounT}{TimE_HEx}00000{Header}"
            FiNal_ToKen_0115 = Header + EnC_PacKeT(JwT_ToKen_, key, iv)
            JwT_ToKen_ = None
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")
            return
        self.AutH_ToKen = FiNal_ToKen_0115
        os.system("clear")
        await self.STarT(self.JwT_ToKen, self.AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid)


def load_accounts(file_path="sb.json"):
    if not os.path.isabs(file_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_path)

    print(f"📂 ফাইল লোড হচ্ছে: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            content = f.read()

        if not content.strip():
            raise ValueError("sb.json ফাইলটি খালি!")

        data = json.loads(content)

        if not isinstance(data, dict):
            raise TypeError(f"sb.json অবশ্যই {{uid: password}} ডিকশনারি হতে হবে")

        accounts = {}
        for k, v in data.items():
            uid = str(k).strip()
            pwd = str(v).strip()
            if uid and pwd:
                accounts[uid] = pwd

        print(f"✅ সফলভাবে {len(accounts)}টি অ্যাকাউন্ট লোড হয়েছে")
        return accounts

    except FileNotFoundError:
        print(f"❌ ভুল: '{file_path}' পাওয়া যায়নি!")
        raise
    except json.JSONDecodeError as e:
        print(f"❌ JSON ভুল: লাইন {e.lineno}, কলাম {e.colno}")
        raise


async def main_async(forced_target, accounts):
    semaphore = asyncio.Semaphore(30)

    asyncio.create_task(periodic_gc())

    async def run_client(uid, pwd):
        async with semaphore:
            client = None
            try:
                client = FF_CLient(uid, pwd, forced_target)
                await client.run()
            except Exception as e:
                print(f" - Client Error [{uid}]: {e}")
            finally:
                del client
                gc.collect()

    account_list = list(accounts.items())
    while True:
        tasks = [run_client(uid, pwd) for uid, pwd in account_list]
        await asyncio.gather(*tasks)


def StarT_SerVer():
    import concurrent.futures
    loop = asyncio.new_event_loop()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=40)
    loop.set_default_executor(executor)
    asyncio.set_event_loop(loop)

    print(render("fuck ", colors=["white", "yellow"], align="center"))
    TexT = f"[TarGeT InFo] > BoTs arE OnLine\n[BoT sTaTus] > [bold green]ConEcTed SuccEssFuLy[/bold green]"
    panel = Panel(
        Align.center(TexT),
        title="[bold yellow]FF - fuck [/bold yellow]",
        border_style="bright_yellow",
        padding=(1, 2),
        expand=False,
    )
    console.print(panel)

    try:
        with open("uid.txt", "r") as f:
            forced_target = f.read().strip()
            if not forced_target:
                forced_target = None
    except:
        forced_target = None

    accounts = load_accounts()

    try:
        loop.run_until_complete(main_async(forced_target, accounts))
    finally:
        executor.shutdown(wait=False)
        loop.close()


if __name__ == "__main__":
    StarT_SerVer()

from odoo import api, fields, models, _
import logging
import psutil
import netifaces as ni
import socket

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.multi
    def _get_host_name(self):
        for record in self:
            host_name = self.env['ir.config_parameter'].get_param('host_name')
            record['host_name'] = f'La dirección IP de {host_name} es {socket.gethostbyname(host_name)}'
    
    @api.multi
    def _compute_server_info(self):
        for record in self:
            record['cpu_usage'] = f'{psutil.cpu_percent()} %'

            mem_info = psutil.virtual_memory()
            record['mem_total'] = f'{(mem_info.total/(1024*1024*1024)):.2f} GB'
            record['mem_used'] = f'{(mem_info.used/(1024*1024*1024)):.2f} GB'
            record['mem_used_percent'] = f'{mem_info.percent} %'

            disk_mem_info = psutil.disk_usage('/')
            record['disk_mem_total'] = f'{(disk_mem_info.total/(1024*1024*1024)):.2f} GB'
            record['disk_mem_used'] = f'{(disk_mem_info.used/(1024*1024*1024)):.2f} GB'
            record['disk_mem_used_percent'] = f'{disk_mem_info.percent} %'
            record['disk_mem_free'] = f'{(disk_mem_info.free/(1024*1024*1024)):.2f} GB'

            ip4_info = ni.ifaddresses('ens3')[ni.AF_INET][0]['addr']
            record['ip4_info'] = f'{(ip4_info)}'
            ip6_info = ni.ifaddresses('ens3')[ni.AF_INET6][0]['addr']
            record['ip6_info'] = f'{(ip6_info)}'
        
    host_name = fields.Char(
        compute=_get_host_name,
        readonly=True
    )
    cpu_usage = fields.Char(
        string="Uso",
        compute=_compute_server_info,
        readonly=True
    )
    mem_total = fields.Char(
        string="Total",
        compute=_compute_server_info,
        readonly=True
    )
    mem_used = fields.Char(
        string="Uso",
        compute=_compute_server_info,
        readonly=True
    )
    mem_used_percent = fields.Char(
        string="Uso(%)",
        compute=_compute_server_info,
        readonly=True
    )
    disk_mem_total = fields.Char(
        string="Total",
        compute=_compute_server_info,
        readonly=True
    )
    disk_mem_used = fields.Char(
        string="Usado",
        compute=_compute_server_info,
        readonly=True
    )
    disk_mem_free = fields.Char(
        string="Libre",
        compute=_compute_server_info,
        readonly=True
    )
    disk_mem_used_percent = fields.Char(
        string="Usado(%)",
        compute=_compute_server_info,
        readonly=True
    )
    ip4_info = fields.Char(
        string="IPv4",
        compute=_compute_server_info,
        readonly=True
    )
    ip6_info = fields.Char(
        string="IPv6",
        compute=_compute_server_info,
        readonly=True
    )

